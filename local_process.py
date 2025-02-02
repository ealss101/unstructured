import os
import dotenv

from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.interfaces import ProcessorConfig
from unstructured_ingest.v2.processes.connectors.local import (
    LocalIndexerConfig,
    LocalDownloaderConfig,
    LocalConnectionConfig,
    LocalUploaderConfig
)
from unstructured_ingest.v2.processes.partitioner import PartitionerConfig
# from unstructured_ingest.v2.processes.chunker import ChunkerConfig  # remove
# from unstructured_ingest.v2.processes.embedder import EmbedderConfig  # remove

# Chunking and embedding are optional.

if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    Pipeline.from_configs(
        context=ProcessorConfig(),
        indexer_config=LocalIndexerConfig(input_path="data"),
        downloader_config=LocalDownloaderConfig(),
        source_connection_config=LocalConnectionConfig(),
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
        # chunker_config=ChunkerConfig(chunking_strategy="by_title"), # remove
        # embedder_config=EmbedderConfig(embedding_provider="huggingface"),  # remove
        uploader_config=LocalUploaderConfig(output_dir="output")
    ).run()
