module.exports = async ({github, context, core}) => {
  let fs = require('fs');
  let {owner, repo} = context.repo;
  let run = context.payload.workflow_run;

  let issue_number = Number(fs.readFileSync('pr-artifacts/pr-info/number', {'encoding': 'utf-8'}).trim());
  if(!Number.isInteger(issue_number) || issue_number <= 0) {
    core.setFailed(`Invalid PR number in pr-info artifact: ${issue_number}`);
    return;
  }
  // The artifact comes from the PR run, so make sure it is not pointing at someone else's PR.
  let {data: pr} = await github.rest.pulls.get({owner, repo, pull_number: issue_number});
  if(pr.head.sha != run.head_sha) {
    core.warning(`PR #${issue_number} head ${pr.head.sha} does not match run head ${run.head_sha}, skipping comment`);
    return;
  }

  let {data: {artifacts}} = await github.rest.actions.listWorkflowRunArtifacts({owner, repo, run_id: run.id});
  let get_artifact_url = (artifact) => `${context.serverUrl}/${owner}/${repo}/actions/runs/${run.id}/artifacts/${artifact.id}`;
  let preview = artifacts.find(a => a.name.startsWith('preview-'));
  let log = artifacts.find(a => a.name == 'sltt-log');

  let comment_body = "";
  if(fs.existsSync('pr-artifacts/sltt-errors/sltt-errors.txt')) {
    comment_body += "SLTT produced errors:\n\n";
    comment_body += fs.readFileSync('pr-artifacts/sltt-errors/sltt-errors.txt', {'encoding': 'utf-8'}) + "\n";
  } else if(run.conclusion != 'success') {
    comment_body += `Check failed, see [workflow run](${run.html_url})\n\n`;
  }
  if(preview) {
    comment_body += `[Download preview](${get_artifact_url(preview)})\n\n`
  }
  if(log) {
    comment_body += `[Download log](${get_artifact_url(log)})\n\n`
  }
  await github.rest.issues.createComment({owner, repo, issue_number, body: comment_body});
}
