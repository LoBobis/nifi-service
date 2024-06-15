import nipyapi


class Flow:
    def __init__(self, flow_id: str, bucket_id: str, location: tuple):
        self._pg = nipyapi.versioning.deploy_flow_version(location=location, flow_id=flow_id,
                                                          reg_client_id="17b22882-0190-1000-e737-24f6b84c5135",
                                                          bucket_id=bucket_id, parent_id=nipyapi.canvas.get_root_pg_id(), version=2)
        self._context_parameter = None

    def add_params(self, params_dict: dict, context_parameter_name: str):
        params = [nipyapi.parameters.prepare_parameter(param_name, value) for param_name, value in params_dict.items()]
        self._context_parameter = nipyapi.parameters.create_parameter_context(name=context_parameter_name,
                                                                              parameters=params)
        nipyapi.parameters.assign_context_to_process_group(pg=self._pg, context_id=self._context_parameter.id)

    def start_flow(self):
        nipyapi.canvas.schedule_process_group(process_group_id=self._pg.id, scheduled=True)

    def stop_flow(self):
        nipyapi.canvas.schedule_process_group(process_group_id=self._pg.id, scheduled=False)

    # def __del__(self):
    #     self.stop_flow()
    #     nipyapi.nifi.ProcessGroupsApi().remove_process_group(id=self._pg.id, version=self._pg.revision.version)
    #
    #     if self._context_parameter:
    #         nipyapi.nifi.ParameterContextsApi().delete_parameter_context(id=self._context_parameter.id, version=self._context_parameter.revision.version)




