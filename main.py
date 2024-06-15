import core.nypi
from core.flow import Flow
from core.utils import get_free_location



for i in range(0,3):
    flow = Flow(flow_id="b4ea1598-e95b-41f5-82c1-1bd0da3857e2", bucket_id="0a1fce16-176a-4ddc-8b2a-e35ae3e778a7",
                location=get_free_location())

    content_name = f"do033{i}"
    flow.add_params(params_dict={"topic_name": "eyal", "kafka_username": "username", "dp_url": "http://url/"},
                    context_parameter_name=content_name)

    flow.start_flow()