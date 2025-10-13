# SSH FAIR Vocabulary Registry: Metadata editor

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

# Introduction

This repository contains the code and basic documentation of one of the components of the FAIR vocabulary registry (i.e., the vocabulary metadata editor).

The FAIR Vocabulary Registry for the Humanities and Social Sciences (SSH) is built in the context of the "Social Sciences and Humanities Open Cloud" project ([SSHOC-NL](https://sshoc.nl/)). This project develops state-of-the-art infrastructure for researchers, in collaboration between [ODISSEI](https://odissei-data.nl/) (Open Data Infrastructure for Social Science and Economic Innovations) and [CLARIAH](https://www.clariah.nl/) (Common Lab Research Infrastructure for the Arts and Humanities).

The SSH FAIR Vocabulary Registry is a one-stop reference service for vocabularies that are relevant to researchers, developers, data managers or curators working on improving the FAIR-ness of research data in the SSH research communities, mostly in the context of SSHOC-NL. It aims to support them in finding, (re)using, publishing and adding vocabularies to the registry.

You are here in one of the repositories that form part of [the architecture](https://registry.vocabs.clariah.nl/about/) of the SSH FAIR vocabulary registry. This specific repository contains the code for the metadata editor. This editor is built using the [CLARIN Component Metadata infrastructure (CMDI)](https://www.clarin.eu/content/cmdi-component-metadata-infrastructure) for the modelling of the vocabularies' metadata schema and the data-entry forms.

Each vocabulary in the SSH FAIR Vocabulary Registry is described according to a metadata schema (which is [here](https://github.com/CLARIAH/vocab-registry-editor/raw/refs/heads/main/data/apps/vocabs/profiles/clarin.eu:cr1:p_1653377925723/clarin.eu:cr1:p_1653377925723.xml), currently in development).

The metadata records which are in the production version of the vocabulary registry are all updated in this Github repository (`/apps/vocabs/profiles/clarin.eu:cr1:p_1653377925723/records`).

# Usage
The vocabulary metadata editor is meant to be used by the curators of the SSH FAIR Vocabulary Registry. Currently, this editing process is moderated by the maintainers of this repository (see contact information below).

The metadata editor, however, can also be run locally (for example, in case that you are interested in seeing how it works, or in creating a (locally stored) vocabulary record yourself). To start the services, navigate to the directory containing your `docker-compose.yml` file and run:
```docker-compose up```.
This will build the images (if they don’t already exist) and start all the services defined in the docker-compose.yml.
In addition, if you want to create a new editor or adapt the existing one to your own purposes, you can find more information at the CLARIN Component Metadata Infrastructure, and also in the [repository of the editor service](https://github.com/knaw-huc/service-huc-editor).

# Documentation
More information about the project and the vocabulary registry can be found here: [https://registry.vocabs.clariah.nl/about/](https://registry.vocabs.clariah.nl/about/).

# Support and roadmap
- Issue tracker: [https://github.com/CLARIAH/vocab-registry-editor/issues](https://github.com/CLARIAH/vocab-registry-editor/issues)
- Contact maintainer: <a href="&#109;a&#105;l&#116;&#111;:&#115;&#116;&#114;&#117;&#99;&#116;&#117;&#114;&#101;&#100;&#45;&#100;&#97;&#116;&#97;&#64;&#100;&#105;&#46;&#104;&#117;&#99;&#46;&#107;&#110;&#97;&#119;&#46;&#110;&#108;">DI Structured Data Team</a>. 
- Roadmap: [https://github.com/orgs/CLARIAH/projects/12](https://github.com/orgs/CLARIAH/projects/12) (note: this project kanban has temporarily private access)