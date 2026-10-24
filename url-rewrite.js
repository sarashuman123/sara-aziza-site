// CloudFront Function (viewer request). Makes S3 behave like a web server for
// clean URLs: /archive/ -> /archive/index.html, /archive -> /archive/index.html.
function handler(event) {
  var request = event.request;
  var uri = request.uri;
  if (uri.endsWith('/')) {
    request.uri = uri + 'index.html';
  } else if (!uri.includes('.')) {
    request.uri = uri + '/index.html';
  }
  return request;
}
