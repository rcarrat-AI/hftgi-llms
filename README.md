# HuggingFace TGI for LLMs in Kubernetes / OpenShift

[HuggingFace Text Generation Inference](https://github.com/huggingface/text-generation-inference) deployments in K8s/OpenShift

## Overview

[Text Generation Inference (TGI)](https://huggingface.co/docs/text-generation-inference/index) is a toolkit for deploying and serving Large Language Models (LLMs). TGI enables high-performance text generation for the most popular open-source LLMs, including Llama, Falcon, StarCoder, BLOOM, GPT-NeoX, and T5.

## Deployment

Tested with A10G (g5.2xlarge) with Spot Instances using a ROSA cluster with 4.13 version and RHODS with 2.14.0

## Models tested

- Flan-T5-XXL
- [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
- [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct)
- Llama2

## Others

- This is just a PoC, not ready for Production!
- Repo is heavily based in the [llm-on-openshift repo](https://github.com/rh-aiservices-bu/llm-on-openshift/tree/main/hf_tgis_deployment). Kudos to them!