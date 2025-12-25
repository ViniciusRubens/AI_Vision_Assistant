# AI Vision Assistant (ViLT)

### About the project

A state-of-the-art multimodal Machine Learning application for Visual Question Answering (VQA), built with a modular architecture, containerized with Docker, and designed for high-performance inference.

This project leverages the **ViLT (Vision-and-Language Transformer)** model to enable users to interact with images using natural language. Unlike traditional image classifiers, this system understands the semantic relationship between vision and text within a single monolithic Transformer.

### Problem

Traditional computer vision models are often limited to pre-defined labels. Extracting specific information from an image (e.g., "What is the dog doing?") usually requires complex, heavy models that demand excessive hardware resources.

### Solution

I implemented the **ViLT-B/32** model within a modularized **FastAPI** REST API. The solution uses **Docker** to ensure the execution environment is identical across any machine and features a modern web interface for seamless user interaction.

### Tech stack

* **Core:** Python 3.11.5
* **ML Framework:** PyTorch & Hugging Face Transformers
* **Backend:** FastAPI (Uvicorn)
* **Infrastructure:** Docker (Ubuntu 24.04)
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Compilers:** Rust (required for tokenizers optimization)

---

### Data source and Pipeline

The model used is [dandelin/vilt-b32-finetuned-vqa](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa), pre-trained on the VQAv2 dataset.

1.  **Frontend:** Captures image (Multipart) and text query (Form-data). 
2.  **Controller:** Validates the input and converts the image to the RGB color space.
3.  **Service:** Performs inference using `torch.no_grad()` for maximum memory efficiency.
4.  **Output:** Returns a structured JSON containing the most probable answer.

---

## Getting Started

### Prerequisites

* Ubuntu 24.04 (or any Linux distribution with Docker).
* Docker installed and configured (non-root access recommended).
* Minimum 8GB RAM recommended for smooth inference.

### Installation

1.  **Clone the repository** (or download https://github.com/ViniciusRubens/AI_Vision_Assistant the files to a local folder).
    ```bash
    git clone git@github.com:ViniciusRubens/AI_Vision_Assistant.git
    cd your-repository-name
    ```

2.  Grant execution permissions to the automation scripts:
    ```bash
    chmod +x build.sh run.sh
    ```

3.  Build the Docker image:
    ```bash
    ./build.sh
    ```

---

## Usage

Follow these instructions to set up a local copy of the project.

To start the system, simply run the execution script:
```bash
./run.sh
```

After that, access in browser the: `http://localhost:3000/`

You will see something like that:

![](/images/image.png)

---

## License

Distributed under the MIT License. See `LICENSE` file for more information.