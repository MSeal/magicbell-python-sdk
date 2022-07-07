# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2022-07-07
### Added
- Add `MagicBell.connect` and `MagicBell.disconnect` methods for more ergonomic connection management.

### Fixed
- Reorder `Notification` types to avoid forward ref issue in pydantic validation

## [1.0.0] - 2022-07-05
First open source release of the SDK.

### Added
- Initial repo setup with basic client and CI
- APIs supported:
  - Create notification
  - Create user
  - Update user
  - Delete user
  - List projects
  - Get project
  - Create project
  - Update project
  - Delete project
  - Updating channel configuration for a project (undocumented)
  - Retrieve channel configuration for a project (undocumented)
  - GraphQL queries
