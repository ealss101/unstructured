import os
import dotenv

from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.interfaces import ProcessorConfig
from unstructured_ingest.v2.processes.connectors.google_drive import (
    GoogleDriveConnectionConfig,
    GoogleDriveAccessConfig,
    GoogleDriveIndexerConfig,
    GoogleDriveDownloaderConfig
)
from unstructured_ingest.v2.processes.partitioner import PartitionerConfig
# from unstructured_ingest.v2.processes.chunker import ChunkerConfig
# from unstructured_ingest.v2.processes.embedder import EmbedderConfig
from unstructured_ingest.v2.processes.connectors.local import LocalUploaderConfig

# Chunking and embedding are optional.

if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    Pipeline.from_configs(
        context=ProcessorConfig(),
        indexer_config=GoogleDriveIndexerConfig(),
        downloader_config=GoogleDriveDownloaderConfig(download_dir=os.getenv("LOCAL_FILE_GOOGLE_DRIVE_DOWNLOAD_DIR")),
        source_connection_config=GoogleDriveConnectionConfig(
            access_config=GoogleDriveAccessConfig(
                service_account_key_path=os.getenv("GCP_SERVICE_ACCOUNT_KEY_FILEPATH"), # Or
                service_account_key=os.getenv("GCP_SERVICE_ACCOUNT_KEY_STRING")
            ),
            drive_id=os.getenv("GOOGLE_DRIVE_FOLDER_ID"),
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
        # chunker_config=ChunkerConfig(chunking_strategy="by_title"),
        # embedder_config=EmbedderConfig(embedding_provider="huggingface"),
        uploader_config=LocalUploaderConfig(output_dir=os.getenv("LOCAL_FILE_GOOGLE_DRIVE_UPLOAD_DIR"))
    ).run()
