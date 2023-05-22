from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "test_py-0522075123",
}

dag = DAG(
    "test_py-0522075123",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `test_py.py`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: test_py.py

op_5e8bb38e_f6d7_4f0c_b2e0_9be54464c0f5 = KubernetesPodOperator(
    name="test_py",
    namespace="default",
    image="continuumio/anaconda3@sha256:a2816acd3acda208d92e0bf6c11eb41fda9009ea20f24e123dbf84bb4bd4c4b8",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'test_py' --cos-endpoint http://90.0.1.37:9000 --cos-bucket dag --cos-directory 'test_py-0522075123' --cos-dependencies-archive 'test_py-5e8bb38e-f6d7-4f0c-b2e0-9be54464c0f5.tar.gz' --file 'test_py.py' "
    ],
    task_id="test_py",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "ust8898865",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "test_py-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)
