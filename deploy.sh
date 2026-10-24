#!/usr/bin/env bash
# Rebuild the site and push it to S3, then tell CloudFront to drop its cache.
# Usage: BUCKET=saraaziza.com DIST_ID=E123ABC ./deploy.sh
# Needs the AWS CLI installed and logged in (aws configure).
set -euo pipefail
cd "$(dirname "$0")"
: "${BUCKET:?set BUCKET to the S3 bucket name}"
: "${DIST_ID:?set DIST_ID to the CloudFront distribution id}"

python3 process_images.py
python3 build.py

# Images and fonts never change under the same name: cache them for a year.
aws s3 sync dist/img "s3://$BUCKET/img" --delete --cache-control "public, max-age=31536000, immutable"
aws s3 sync dist/static "s3://$BUCKET/static" --delete --cache-control "public, max-age=31536000, immutable" --exclude "style.css" --exclude "site.js"
# HTML, CSS and JS: short cache so edits show up quickly.
aws s3 sync dist "s3://$BUCKET" --delete --exclude "img/*" --exclude "static/*" --cache-control "public, max-age=300"
aws s3 cp dist/static/style.css "s3://$BUCKET/static/style.css" --cache-control "public, max-age=300" --content-type "text/css"
aws s3 cp dist/static/site.js "s3://$BUCKET/static/site.js" --cache-control "public, max-age=300" --content-type "application/javascript"

aws cloudfront create-invalidation --distribution-id "$DIST_ID" --paths "/*" >/dev/null
echo "deployed to https://saraaziza.com"
