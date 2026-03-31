import argparse
import logging
import os
from tokenize import group
from resume_generator import ResumeGenerator
from dotenv import load_dotenv

def main():
    config = load_config()
    setup_logger(config)
    logger = logging.getLogger(__name__)
    logger.debug("Application started with configuration: %s", config)

    parser = argparse.ArgumentParser(description="A tool to generate Word documents from templates and input data.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-t",
        "--template",
        type=str,
        help="Path to the Word template file"
    )

    args = parser.parse_args()

    if args.template:
        logger.info("Using template: %s", args.template)
        full_template_path = os.path.join(config["TEMPLATE_FOLDER"], args.template)
        resume_generator = ResumeGenerator(template=full_template_path, 
                                           input_folder=config["INPUT_FOLDER"],                                           
                                           header=config["INPUT_HEADERS"],
                                           dtypes=config["INPUT_DATA_TYPES"],
                                           output_folder=config["OUTPUT_FOLDER"],
                                           pooling_delay=float(config["POOLING_DELAY"]))
        resume_generator.generate_resumes()
    else:
        logger.error("No template provided. Exiting.")
        return


def load_config():
    load_dotenv()

    return {
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO").upper(),
        "POOLING_DELAY": int(os.getenv("POOLING_DELAY", 30)),
        "TEMPLATE_FOLDER": os.getenv("TEMPLATE_FOLDER", "./templates"),
        "INPUT_FOLDER": os.getenv("INPUT_FOLDER", "./input"),
        "INPUT_HEADERS": os.getenv("INPUT_HEADERS").split(",") if os.getenv("INPUT_HEADERS") else [],
        "INPUT_DATA_TYPES": eval(os.getenv("INPUT_DATA_TYPES", "{}")),
        "OUTPUT_FOLDER": os.getenv("OUTPUT_FOLDER", "./output")
    }


def setup_logger(config): 
    log_level = config["LOG_LEVEL"]
    numeric_level = getattr(logging, log_level, logging.INFO)
    logging.basicConfig(level=numeric_level)

if __name__ == "__main__":
    main()