# Contributing Guidelines

## Checklist
1. All functions must have documentations (comments at the start of it), provided the function name is not indicative of the exact work it does or the function length is more than 5 lines.
2. Console, print statements etc should be commented before moving to production. 
3. pdb statement must not be there.

## Raising a PR

### Branch Flow === feature_branches -> master -> master_prod
```
1. main will host the incoming stable code at a weekly/biweekly basis, with testing completed at development side.
2. prod - in production.
```

### Guidelines
1. All feature branchs must be made from the **master** branch, and all PR's raised against it.
2. PR's must always be **squashed and merged** to the master branch.
3. Further PR's must **not be** squashed and merged, else it will break the commit histories.
4. All PR's must have a concise message along with Ticket Number/Jira Ticket ID.
5. Branch names must indicate the code/Jira Ticket Number/ issues etc.

## Code Linting
```
Follow the same code structure as already provided.
Frontend
    Use Prettier (VS Code Extension) to update code on the fly.

Backend
    Pycharm
```

