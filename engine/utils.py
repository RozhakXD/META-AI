import requests
import secrets
import uuid
import re
import time
import json
import random
from requests_toolbelt import MultipartEncoder

def generate_boundary() -> str:
    return "----WebKitFormBoundary" + secrets.token_urlsafe(16)

def get_response_from_meta_ai(message: str) -> str:
    with requests.Session() as session:
        session.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Host": "www.meta.ai",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        response = session.get("https://www.meta.ai/?utm_source=llama_meta_site&utm_medium=web&utm_content=Llama_hero&utm_campaign=Sept_moment", allow_redirects=True)

        datr = session.cookies.get_dict()["datr"]
        abra_csrf = re.search(r'"abra_csrf":{"value":"([^"]+)"', response.text).group(1)
        lsd = re.search(r'"LSD",\[\],{"token":"([^"]+)"}', response.text).group(1)

        data = {
            "fb_api_caller_class": "RelayModern",
            "server_timestamps": True,
            "doc_id": 8803207726462995,
            "lsd": f"{lsd}",
            "fb_api_req_friendly_name": "useAbraAcceptTOSForTempUserMutation",
            "variables": json.dumps(
                {
                    "dob": "2004-01-01",
                    "icebreaker_type": "TEXT_V2",
                    "__relay_internal__pv__AbraFileUploadsrelayprovider": False,
                    "__relay_internal__pv__AbraSufaceNuxIDrelayprovider": "12177",
                    "__relay_internal__pv__AbraQPFileUploadTransparencyDisclaimerTriggerNamerelayprovider": "meta_dot_ai_abra_web_file_upload_transparency_disclaimer",
                    "__relay_internal__pv__AbraUpsellsKillswitchrelayprovider": True,
                    "__relay_internal__pv__WebPixelRatiorelayprovider": 1,
                    "__relay_internal__pv__AbraIcebreakerImagineFetchCountrelayprovider": 20,
                    "__relay_internal__pv__AbraImagineYourselfIcebreakersrelayprovider": False,
                    "__relay_internal__pv__AbraEmuReelsIcebreakersrelayprovider": False,
                    "__relay_internal__pv__AbraQueryFromQPInfrarelayprovider": False
                }
            )
        }

        session.headers.update(
            {
                "Referer": "https://www.meta.ai/?utm_source=llama_meta_site&utm_medium=web&utm_content=Llama_hero&utm_campaign=Sept_moment",
                "Content-Length": f"{len(str(data))}",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": f"datr={datr}; wd=1280x585; dpr=1.5; ps_l=1; ps_n=1; abra_csrf={abra_csrf}",
                "Origin": "https://www.meta.ai",
                "Sec-Fetch-Dest": "empty",
                "X-FB-LSD": f"{lsd}",
                "Accept": "*/*",
                "Sec-Fetch-Mode": "cors",
                "X-ASBD-ID": "129477",
                "Sec-Fetch-Site": "same-origin",
                "X-FB-Friendly-Name": "useAbraAcceptTOSForTempUserMutation",
            }
        )

        response2 = session.post("https://www.meta.ai/api/graphql/", data=data, allow_redirects=False)

        session.headers.pop('Content-Length')
        session.headers.pop('Content-Type')
        session.headers.update(
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Sec-Fetch-Dest": "document",
                "dpr": "1.5",
                "Sec-Fetch-Mode": "navigate",
            }
        )

        response3 = session.get("https://www.meta.ai/", allow_redirects=True)

        accessToken = re.search(r'accessToken":"([^"]+)"', response3.text)
        if accessToken:
            accessToken = accessToken.group(1)
        else:
            accessToken = re.search(r'access_token":"([^"]+)"', response2.text).group(1)

        boundary = generate_boundary()
        multipart_data = MultipartEncoder(
            fields={
                "access_token": f"{accessToken}",
                "lsd": f"{lsd}",
                "fb_api_caller_class": "RelayModern",
                "fb_api_req_friendly_name": "useAbraSendMessageMutation",
                "variables": json.dumps(
                    {
                        "message": {
                            "sensitive_string_value": message,
                        },
                        "externalConversationId": f"{uuid.uuid4()}",
                        "offlineThreadingId": str((int(time.time() * 1000) << 22) | (random.getrandbits(64) & ((1 << 22) - 1)))
                    }
                ),
                "server_timestamps": "true",
                "doc_id": "9641279242553711"
            },
            boundary=boundary
        )

        body = multipart_data.to_string()

        session.headers.update(
            {
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "Referer": "https://www.meta.ai/",
                "Content-Length": f"{len(body)}",
                "Cookie": f"datr={datr}; wd=1280x585; dpr=1.5; ps_l=1; ps_n=1; abra_csrf={abra_csrf}",
                "Host": "graph.meta.ai",
                "Accept": "*/*",
                "Origin": "https://www.meta.ai",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            }
        )

        response4 = session.post("https://graph.meta.ai/graphql?locale=user", data=body, allow_redirects=False)

        for data in response4.text.splitlines():
            if '"streaming_state":"LLM_DONE"' in str(data):
                snippet = json.loads((data))['data']['node']['bot_response_message']['snippet']
                return snippet
            else:
                continue
        return False