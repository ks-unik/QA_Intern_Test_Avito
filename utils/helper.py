import allure
import json
from allure_commons.types import AttachmentType

class Helper:

    def attach_response(self,response):
        response = json.dumps(response, ensure_ascii=False, indent=4)
        allure.attach(
        body=response,
        name="API Response",
        attachment_type=AttachmentType.JSON
    )
        
        def attach_step_status(self, step_name: str, status_code: int):
            print(f"[STEP] {step_name} — статус код {status_code}")
            with allure.step(f"{step_name} — статус код {status_code}"):
                pass