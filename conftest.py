import pytest
import logging
from datetime import datetime
from pathlib import Path

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_DIR = "output"


# Configure the logger at module level
def setup_logger():
    """Setup simple logger for pytest session"""
    # Create log directory
    log_dir = Path(OUTPUT_DIR)
    log_dir.mkdir(exist_ok=True)

    # Create log file with timestamp
    log_file = log_dir / f"pytest_{TIMESTAMP}.log"

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(log_file, mode='w', encoding='utf-8'),
            logging.StreamHandler()  # Remove this line if you don't want console output
        ],
        force=True  # Override any existing configuration
    )

    return logging.getLogger(__name__)


# Configure HTML report automatically
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: marks tests as smoke tests (quick sanity checks)"
    )
    # Create reports directory
    report_dir = Path(OUTPUT_DIR)
    report_dir.mkdir(exist_ok=True)

    # Set HTML report path with timestamp
    report_path = report_dir / f"pytest_{TIMESTAMP}.html"
    config.option.htmlpath = str(report_path)
    config.option.self_contained_html = True


# Initialize logger at session start
@pytest.fixture(scope="session", autouse=True)
def session_logger():
    """Initialize logger for entire pytest session"""
    logger = setup_logger()
    logger.info("=" * 50)
    logger.info("PYTEST SESSION STARTED")
    logger.info("=" * 50)

    yield logger

    logger.info("=" * 50)
    logger.info("PYTEST SESSION COMPLETED")
    logger.info("=" * 50)


# Simple function to get logger from anywhere
def get_logger():
    """Get the configured logger from anywhere in your tests"""
    return logging.getLogger(__name__)


# Convenience function for even simpler usage
def log(message):
    """Simple log function - call from anywhere"""
    get_logger().info(message)
