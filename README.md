# INF2102-PFP

Projeto final de programação para o curso INF2102 - Um orquestrador MLOps de cargas de trabalho para um model de detecção de pulsares

Obs: O treinamento do modelo deve ocorrer locamente, fora da infraestrutura gerenciada

Tutorial de criação de container para AWS SageMaker MLOps <https://aws.amazon.com/blogs/machine-learning/train-and-host-scikit-learn-models-in-amazon-sagemaker-by-building-a-scikit-docker-container/>
Projeto exemplo de modelo scikit learn no AWS SageMaker MLOps <https://github.com/aws/amazon-sagemaker-examples/tree/main/advanced_functionality/scikit_bring_your_own>
Projeto no guia de implementação <https://docs.aws.amazon.com/solutions/latest/mlops-workload-orchestrator/solution-overview.html>

## Pré-requisitos

- Python 3.10
- Python 3.10 venv
- Uma conta AWS válida
- AWS CLI v2

### Execução do jupyter notebook para criação do modelo e projeto orientado a objetos

- Abra o arquivo pulsar_complete_project.ipynb e executar suas células

### Montagem do container docker para execução no SageMaker MLOps

- Configurar uma sessão de linha de comando AWS

```bash
aws configure
aws configure set region us-east-1
```

- Realizar o build do container

```bash
cd container/
./build_and_push.sh random_forest
```

- Logo, teremos o id container, nesses moldes <aws_account_number>.dkr.ecr.us-east-1.amazonaws.com/random_forest, para criarmos um sagemaker endpoint
- Agora, já podemos realizar testes locais de execução

```bash
cd local_test/
chmod +x *.sh
./train_local.sh random_forest
```

- Abra uma nova aba do terminal no mesmo projeto e diretório (`local_test/`) e suba o servidor de inferência

```bash
./serve_local.sh random_forest
```

- Na aba original, execute o script de predição automática

```bash
./predict.sh payload.csv text/csv 
```

- Pare o container quando estiver satisfeito

```bash
docker ps -a
docker kill <CONTAINER_ID>
```

### Construa a solução de implantação

- Siga os passos do guia de implementação na seguinte seção <https://docs.aws.amazon.com/pt_br/solutions/latest/mlops-workload-orchestrator/step-1-launch-the-stack.html>
- Será necessário o login na sua conta AWS na região de us-east-1 North Virginia
- Preencha os campos de Stack Name com o nome customizado da stack e os campos Required (até o dia 25/11/2023, o email era o único mandatório apenas para notificações de status)
*ATENÇÃO* - O custo geral da infrestrutura é de $374.57. Ao final dos testes, por favor, destrua a infraestrutura criada
- Acompanhe a criação da infraestrutura na aba de Status do CloudFormation
- Na aba Outputs, haverá a localização para upload dos artefatos do modelo e a url para checagem do status da pipeline
- Vamos agora, salvar o nosso modelo, em artefato joblib, para o bucket criado pelo stack set

```bash
tar czvf model.tar.gz random-forest-pulsar-model.pkl
aws s3 cp model.tar.gz s3://<bucket-name>
```

- Para executar a criação da pipeline, podemos executar localmente como um `POST` para o path `/provisionpipeline` na url do output do change set com nome `PipelineOrchestrationLambdaRestApiEndpoint*`. Contudo, é preciso remover a autenticação para os testes seguindo esse post <https://repost.aws/knowledge-center/iam-authentication-api-gateway>
- E também utilizar o seguinte body no payload de requisição:

```json
{
  "pipeline_type": "byom_realtime_custom",
  "custom_image_uri": "021707296066.dkr.ecr.us-east-1.amazonaws.com/random_forest",
  "model_name": "pulsar",
  "model_artifact_location": "model.tar.gz",
  "data_capture_location": "<bucket-name>/data",
  "inference_instance": "ml.m5.large",
  "endpoint_name": "pulsar"
}
```

- Com uma execução com sucesso, o retorno será dessa forma:

```json
{
  "message": "success: stack creation started", 
  "pipeline_id": "arn:aws:cloudformation:<region>:<account-id>:stack/<stack-id>"
}
```

- Enfim, para checarmos o status da pipeline, executamos um `POST` para o path `\pipelinestatus` com o seguinte body:

```json
{
  "pipeline_id": "arn:aws:cloudformation:<region>:<account-id>:stack/<stack-id>"
}
```

- Após o retorno com a pipeline já provisionada, com uma resposta do tipo:

```json
{
  "message": "Pipeline <stack-name> is already provisioned. Updating template parameters.", 
  "pipeline_id": "arn:aws:cloudformation:<region>:<account-id>:stack/<stack-id>"
}             
```

- Devemos esperar a criação do enpoint para inferencia, basta olharmos no tempalte de cloudformation do tipo `mlops-pipeline-*-byompipelinerealtimecustom` terminar