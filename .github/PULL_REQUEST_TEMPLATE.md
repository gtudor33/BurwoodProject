<!-- EDIT ME: If there are related PRs, please uncomment and link to the related PRs.

## :satellite: Related PR / Commit

-->

## :clipboard: Reviewer Documentation and Change Log

<!-- If this is a new feature, please link to the PRD file, if unsure contact the PM. -->
<!-- If this is a new FSM, please include a graph of the FSM -->
<!-- If this is PR contains new complex SQL queries, please include EXPLAIN ANALYZE output -->
<!-- Describe your changed here -->
<!-- Add code snippets, logs outputs, db results etc that can be useful -->

<!-- EDIT ME: If this is related to a bug, then uncomment and fill out the following two sections

### Before changes
It was broken

### After changes
I fixed it!
-->

## :eyes: Testing & Deploy Steps

<!--
How was this tested locally / end to end to ensure the functionality is working properly? What steps can reviewers take to test this locally?

What services and/or metrics should be observed after deployment? If functionality is hitting existing or new endpoints, DB or service metrics for all affected services should be observed, please describe them below.
-->

## :pencil2: Reminders checklist

1. [ ] Ran `make style` before push

2. [ ] Ran `make build test` before push

3. [ ] Contains DB migration - `db_init` file was updated

4. [ ] Contains config file changes - `.tpl`,` meta-*`, `.conf`, `.json`, `example.env`, `consul` and `vault` were updated

5. [ ] Ran `docker-compose up {service}-clean` or `docker-compose up {service}` and service starts up.

6. [ ] Backfill Scripts are committed even if run locally.

7. [ ] Any new dependencies are added to the `meta-*.yml` files.

8. [ ] Contains endpoints changes - openapi docs were updated.

<!-- feel free to add more-->
