module.exports = ({github, context}) => {
  let fs = require('fs');
  let comment_body = "";
  if(fs.existsSync('sltt-errors.txt')) {
    comment_body += "SLTT produced errors:\n\n";
    comment_body += fs.readFileSync('sltt-errors.txt', {'encoding': 'utf-8'}) + "\n";
  }
  if(process.env.PREVIEW_URL != "") {
    comment_body += `[Download preview](${process.env.PREVIEW_URL})\n\n`
  }
  if(process.env.LOG_URL != "") {
    comment_body += `[Download log](${process.env.LOG_URL})\n\n`
  }
  github.rest.issues.createComment({
    owner: context.repo.owner,
    repo: context.repo.repo,
    issue_number: context.issue.number,
    body: comment_body
  });
}
