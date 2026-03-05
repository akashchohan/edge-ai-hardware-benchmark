# Edge AI Hardware Benchmark

This project evaluates the performance of machine learning models on low-power embedded computing platforms used for edge AI applications.

The focus is on measuring inference latency, power efficiency, and model performance when deployed on constrained hardware.

## Motivation

Edge computing devices such as Jetson and Raspberry Pi are increasingly used in robotics, IoT systems, and Earth Observation platforms. Understanding their performance characteristics for AI workloads is essential for deploying models in real-world environments.

## Objectives

- Benchmark inference performance of lightweight AI models
- Compare CPU and GPU inference performance
- Evaluate model quantisation and optimisation techniques
- Analyse power-performance trade-offs

## Benchmark Platforms

- NVIDIA Jetson Nano / Jetson Orin Nano
- Raspberry Pi 4
- Raspberry Pi Zero

## Metrics

- Inference latency
- Frames per second (FPS)
- Energy consumption
- Model accuracy vs speed trade-off

## Tools

Python  
PyTorch  
ONNX Runtime  
TensorRT (future testing)

## Future Work

- Benchmark multiple computer vision models
- Evaluate quantised model performance
- Create reproducible benchmarking scripts
