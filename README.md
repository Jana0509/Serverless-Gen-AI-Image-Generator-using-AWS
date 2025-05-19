# Serverless-Gen-AI-Image-Generator-using-AWS
This project is a fully serverless application that generates AI-powered images based on text prompts using Amazon Bedrock's Stable Diffusion model.

## Architecture

![Architecture](https://github.com/user-attachments/assets/13beba66-7f1c-429f-a280-90a88def5976)



## 🧰 Key AWS Services Used
🔹Amazon Bedrock – Text-to-image generation using GenAI (Stable Diffusion)

🔹AWS Lambda – Orchestration with fully serverless compute

🔹Amazon S3 – Scalable object storage with secure delivery via presigned URLs

🔹Amazon DynamoDB – Logging and tracking of prompts and statuses

🔹IAM Roles & Policies – Secure service-to-service communication

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
```

###  Real-World Use Cases
This architecture can be applied across multiple industries:

🎨 Marketing & Advertising – On-demand creative generation
🛍️ E-Commerce – Automated product visuals
📰 Publishing & Blogging – AI-powered article illustrations
🎮 Gaming – Visual prototyping
🎓 Education – Teaching materials or concept illustrations
🏥 Healthcare (Non-clinical) – Patient communication visuals
💡 Innovation Labs – Ideation & design exploration

### ✅ Conclusion
This project enhanced my practical understanding of how to combine GenAI and serverless technologies in a powerful, production-ready workflow.
