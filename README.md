# HuggingFace TGI for LLMs in Kubernetes / OpenShift with GitOps

[HuggingFace Text Generation Inference](https://github.com/huggingface/text-generation-inference) deployments in K8s/OpenShift with GitOps!

![LLM0](/assets/llm0.png)

## Overview

[Text Generation Inference (TGI)](https://huggingface.co/docs/text-generation-inference/index) is a toolkit for deploying and serving Large Language Models (LLMs). TGI enables high-performance text generation for the most popular open-source LLMs, including Llama, Falcon, StarCoder, BLOOM, GPT-NeoX, and T5.

The aim of this repository is to easily deploy our LLMs in OpenShift or Kubernetes clusters using GitOps: 

![LLM0](/assets/llm1.png)

## Requirements

- ROSA or OpenShift Clusters (can be also deployed in K8s with some tweaks)
- GPU available (24gb vRAM recommended)
- Node Feature Discovery Operator
- NVIDIA GPU Operator
- ArgoCD / OpenShift GitOps

Tested with A10G (g5.2xlarge) with Spot Instances using a ROSA cluster with 4.13 version and RHODS with 2.14.0

## Models tested

- [Flan-T5-XXL](https://huggingface.co/google/flan-t5-xxl)
- [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
- [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct)
- [Llama2-7B-Chat-HF](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)

## Extra Notes

- This is just a PoC, not ready for Production!
- Repo is heavily based in the [llm-on-openshift repo](https://github.com/rh-aiservices-bu/llm-on-openshift/tree/main/hf_tgis_deployment). Kudos to the team!