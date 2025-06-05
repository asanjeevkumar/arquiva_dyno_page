# My Dynamic String Service

Hey there! I made this service that let you change a string without redeploying. I used FastAPI because I worked with it before in another assessment.

## Stuff I Used
I used FastAPI for the backend in Python. For frontend I kept it simple with just HTML, CSS and JavaScript. For testing I used pytest. I used Black to format the code and pip for managing packages. Make helps me run common commands easily.

## How It Works
The FastAPI app handles REST API calls for string updates, shows the webpage using a template, serves static files and checks inputs using Pydantic. The String Controller keeps the string in memory, has the update function and handles business logic. The UI is simple with a clean design, updates without page reload, handles errors and shows success messages.

## Infrastructure as Code (Terraform)
I chose Terraform for infrastructure because it's declarative and works well with AWS. I've set up a bunch of AWS resources to host our website. We got an S3 bucket for the static website, which is pretty cool. Then I added CloudFront for CDN and HTTPS, which makes the site load faster and more secure. I also included Route 53 for domain management, but that's optional.  we're using another S3 bucket for Terraform state and a DynamoDB table for state locking, which is super important for team work.

For the Terraform config, I'm using AWS provider version 5.0 (or something close to that). The state is stored in S3, which is great for team collaboration. I named all the resources based on the environment, so we can have dev and prod running at the same time. The website bucket is public (which is fine for static websites), and I set up CloudFront to redirect everything to HTTPS. If you want to use a custom domain, that's supported too through Route 53.

## CI/CD Pipeline (GitHub Actions)
I set up GitHub Actions for automated testing and deployment, which is really handy. The pipeline runs whenever someone pushes to main or creates a pull request. It also triggers when someone changes anything in the terraform folder or the workflow file itself. Pretty neat, right?

The pipeline has several stages. First, it checks out the code (obviously). Then it sets up Terraform using the official HashiCorp action. On pull requests, it checks if the Terraform code is properly formatted. After that, it initializes Terraform and validates the configuration. For pull requests, it creates a plan but doesn't apply it. But when changes are pushed to main, it automatically applies the changes. I know, it sounds scary, but it works!

For environments, I kept it simple. Pull requests use the dev environment, and the main branch uses prod. The AWS credentials are stored in GitHub Secrets (which is more secure than putting them in the code). I set the region to eu-west-2 because that's where our other stuff is. I think it's in London, but don't quote me on that!

## Why I Picked FastAPI
FastAPI is fast and modern. It has built in API docs which is nice. The type checking helps catch errors early. It supports async operations and testing is easy. The bad parts are it's less popular than Django, has fewer ready made features and a smaller community. I thought about using Django but it's too big for this. Flask is good but not as modern as FastAPI.

## Why I Store in Memory
Storing in memory is simple and fast. We don't need any extra software and it's good for showing how it works. The problems are data is lost when server restarts, it won't work with many servers and there's no backup. I thought about using a database but it's too complex. Redis would be good but too much for this. File storage is simple but too slow.

## Why One Page
The single page approach is simple for users. There's no need to reload the page, updates are fast and the server doesn't work too hard. The limitations are it only handles one string, there's no history of changes and no login system. I thought about making it multi-page but that's too complex. React would be too much for this simple thing.

## What's Missing for Cloud
For scaling we don't have multi-server support, load sharing, health checks or monitoring. Security is basic with no login system, request limits, input cleaning or HTTPS. Reliability is limited with no logs, backup, disaster plan or high availability.

## Cloud Options I Looked At
For AWS we could use Elastic Beanstalk, RDS, CloudWatch, Route 53 and CloudFront. Azure offers App Service, Azure SQL, Application Insights and Azure CDN. Google Cloud has App Engine, Cloud SQL, Stackdriver and Cloud CDN.

## Things I'd Add Later
For better storage we could use a database, add data migration and implement caching. Security improvements would include a login system, request limits, better input cleaning, HTTPS and API keys. For scaling we need load sharing, health checks, auto-scaling, caching and CDN. Monitoring needs better logs, metrics, alerts, performance tracking and error tracking. User features could include change history, undo/redo, user settings, better errors and loading states. Dev tools would need CI/CD, more tests, code quality checks, better docs and development tools.

## Final Thoughts
Made it simple but it works. Shows how to update string without redeploy. Used FastAPI from previous experience. Memory storage is simple but real world needs database. Code is easy to add more stuff later. Real use needs all the things above to be strong and safe. Learned a lot making this. Hope you like it. Ask if you want to know more about how it works or why I chose things. 