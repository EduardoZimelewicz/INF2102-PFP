# INF2102-PFP

Projeto final de programação para o curso INF2102 - Um orquestrador MLOps de cargas de trabalho para um model de detecção de pulsares

Obs: O treinamento do modelo deve ocorrer locamente, fora da infraestrutura gerenciada

Projeato no guia de implementação <https://docs.aws.amazon.com/solutions/latest/mlops-workload-orchestrator/solution-overview.html>

## Pré-requisitos

- Python 3.10
- Python 3.10 venv
- Uma conta AWS válida
- AWS CLI v2

### Execução do jupyter notebook para criação do modelo e projeto orientado a objetos

- Abra o arquivo pulsar_complete_project.ipynb e executar suas células

### Construa a solução de implantação

- Siga os passos do guia de implementação na seguinte seção <https://docs.aws.amazon.com/pt_br/solutions/latest/mlops-workload-orchestrator/step-1-launch-the-stack.html>
- Será necessário o login na sua conta AWS na região de us-east-1 North Virginia
- Preencha os campos de Stack Name com o nome customizado da stack e os campos Required (até o dia 25/11/2023, o email era o único mandatório apenas para notificações de status)
*ATENÇÃO* - O custo geral da infrestrutura é de $374.57. Ao final dos testes, por favor, destrua a infraestrutura criada
- Acompanhe a criação da infraestrutura na aba de Status do CloudFormation
- Na aba Outputs, haverá a localização para upload dos artefatos do modelo e a url para checagem do status da pipeline
- Vamos agora, salvar o nosso modelo, em artefato joblib, para o bucket criado pelo stack set

```bash
tar czvf model.tar.gz model_pulsar.joblib
aws s3 cp model.tar.gz s3://<bucket-name>
```

- Para executar a criação da pipeline, podemos executar localmente como um `POST` para o path `/provisionpipeline` na url do output do change set com nome `PipelineOrchestrationLambdaRestApiEndpoint*`. Contudo, é preciso remover a autenticação para os testes seguindo esse post <https://repost.aws/knowledge-center/iam-authentication-api-gateway>
- E também utilizar o seguinte body no payload de requisição:

```json
{
"pipeline_type": "byom_realtime_builtin",
"model_framework": "sklearn",
"model_framework_version": "1.2-1",
"model_name": "pulsar",
"model_artifact_location": "model.tar.gz",
"data_capture_location": "<bucket_name>/<prefix>",
"inference_instance": "ml.m5.large",
"endpoint_name": "pulsar"
}
```

{
"pipeline_type": "byom_realtime_builtin",
  "model_framework": "sklearn",
  "model_framework_version": "1.2-1",
  "model_name": "pulsar",
  "model_artifact_location": "model.tar.gz",
  "data_capture_location": "inf2102-mlops-orchestrato-pipelineassets8069ce4301-gtlls1kvsd7a/data",
  "inference_instance": "ml.m5.large",
  "endpoint_name": "pulsar"
}

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

- Devemos esperar a criação do enpoint para inferencia, basta olharmos no tempalte de cloudformation do tipo `mlops-pipeline-*-byompipelinerealtimebuiltin` terminar