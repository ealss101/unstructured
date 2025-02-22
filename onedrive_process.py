import os
import dotenv

from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.interfaces import ProcessorConfig

from unstructured_ingest.v2.processes.connectors.onedrive import (
    OnedriveIndexerConfig,
    OnedriveDownloaderConfig,
    OnedriveConnectionConfig,
    OnedriveAccessConfig
)

from unstructured_ingest.v2.processes.connectors.local import LocalConnectionConfig
from unstructured_ingest.v2.processes.partitioner import PartitionerConfig

if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    Pipeline.from_configs(
        context=ProcessorConfig(),
        indexer_config=OnedriveIndexerConfig(path=os.getenv("ONEDRIVE_PATH")),
        downloader_config=OnedriveDownloaderConfig(
            download_dir=os.getenv("LOCAL_FILE_ONE_DRIVE_DOWNLOAD_DIR")
        ),
        source_connection_config=OnedriveConnectionConfig(
            access_config=OnedriveAccessConfig(
                client_cred=os.getenv("ONEDRIVE_CLIENT_CRED")
            ),
            client_id=os.getenv("ONEDRIVE_CLIENT_ID"),
            tenant=os.getenv("ONEDRIVE_TENANT"),
            user_pname=os.getenv("ONEDRIVE_USER_PNAME"),
            authority_url=os.getenv("ONEDRIVE_AUTHORITY_URL")
        ),
        partitioner_config=PartitionerConfig(
            partition_by_api=True,
            api_key=os.getenv("UNSTRUCTURED_API_KEY"),
            partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
            strategy="hi_res",
            additional_partition_args={
                "split_pdf_page": True,
                "split_pdf_allow_failed": True,
                "split_pdf_concurrency_level": 15
            }
        ),
        destination_connection_config=LocalConnectionConfig()
    ).run()
