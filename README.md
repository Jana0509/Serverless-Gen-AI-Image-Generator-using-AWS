# Serverless-Gen-AI-Image-Generator-using-AWS
Serverless Gen-AI Image Generator using AWS



# 🖼️ Serverless Gen-AI Image Generator using AWS

This project is a fully serverless application that generates AI-powered images based on text prompts using Amazon Bedrock's Stable Diffusion model.

## 🔧 Tech Stack

- AWS Lambda
- Amazon Bedrock (Stable Diffusion XL)
- Amazon S3
- Amazon DynamoDB
- IAM Roles & Policies

## 🔁 Workflow

1. User sends a prompt to the API Gateway → Lambda.
2. Lambda calls Bedrock to generate an image.
3. Image (base64) is decoded and uploaded to S3.
4. A presigned URL is returned to the user.
5. Prompt and status are logged in DynamoDB.

## 💵 Cost Estimate (10 Requests)

> Estimated cost: **~$0.22 for 10 image generations** using Bedrock, Lambda, S3, and DynamoDB (excluding free tier).

## ✅ Example Event Payload

```json
{
  "prompt": "A futuristic city skyline at night"
}
