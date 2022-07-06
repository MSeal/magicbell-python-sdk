import magicbell


class TestListProjects:
    async def test_response_is_parsed_properly(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.projects.list_projects(workspace_id=42)
        project = response.projects[0]

        assert project.id == 1
        assert project.workspace.id == 42


class TestGetProject:
    async def test_response_is_parsed_properly(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.projects.get_project(workspace_id=42, project_id=1)
        project = response.project

        assert project.id == 1
        assert project.workspace.id == 42


class TestCreateProject:
    async def test_response_is_parsed_properly(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.projects.create_project(
            workspace_id=42,
            project_input=magicbell.WrappedProjectInput(
                project=magicbell.ProjectInput(name="Test Project", hmac_enabled=True)
            ),
        )
        project = response.project

        assert project.id == 1
        assert project.workspace.id == 42


class TestUpdateProject:
    async def test_response_is_parsed_properly(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.projects.update_project(
            workspace_id=42,
            project_id=1,
            project_input=magicbell.WrappedProjectInput(
                project=magicbell.ProjectInput(name="Test Project", hmac_enabled=True)
            ),
        )
        project = response.project

        assert project.id == 1
        assert project.workspace.id == 42


class TestDeleteProject:
    async def test_response_is_parsed_properly(self, magicbell_client: magicbell.MagicBell):
        await magicbell_client.projects.delete_project(workspace_id=42, project_id=1)


class TestDeleteProjectDetailed:
    async def test_response_is_accessible(self, magicbell_client: magicbell.MagicBell):
        response = await magicbell_client.projects.delete_project_detailed(
            workspace_id=42, project_id=1
        )
        assert response.status_code == 200
        assert response.json_content() == {"message": "Successfully deleted project"}
