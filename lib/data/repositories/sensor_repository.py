import json
import os
import urllib.error
import urllib.request

from typing import Any

from lib.domain.models.sensor_reading_model import SensorReadingModel


class SensorRepository:
    """SSOT para leitura remota do sensor via API."""

    _endpoint = "https://admin-devices.devskin.com/api/iot/readings"
    _device_id = "SENSOR01"
    _token = os.environ.get("SENSOR_API_TOKEN", "sk_0pVq63cC_OLNuRsibWdPtEmYnLaGHdBm")
    _auth_scheme = os.environ.get("SENSOR_API_AUTH_SCHEME", "Bearer")

    def read_sensor(self) -> SensorReadingModel:
        if not self._token:
            return SensorReadingModel(
                value=None,
                status_message="Token da API não informado. Defina SENSOR_API_TOKEN.",
                success=False,
            )

        url = f"{self._endpoint}?device_id={self._device_id}"
        headers = {
            "Authorization": f"{self._auth_scheme} {self._token}",
            "Accept": "application/json",
            "User-Agent": "FletSensorClient/1.0",
        }
        request = urllib.request.Request(url, headers=headers, method="GET")

        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status != 200:
                    raise ValueError(f"HTTP {response.status}: {response.reason}")

                raw_payload = response.read().decode("utf-8")
                payload = json.loads(raw_payload)
                sensor_value = self._extract_value(payload)

                return SensorReadingModel(
                    value=sensor_value,
                    status_message="Leitura feita com sucesso",
                    success=True,
                )

        except urllib.error.HTTPError as error:
            return SensorReadingModel(
                value=None,
                status_message=f"HTTP {error.code}: {error.reason}",
                success=False,
            )
        except urllib.error.URLError as error:
            return SensorReadingModel(
                value=None,
                status_message=f"Rede: {error.reason}",
                success=False,
            )
        except (json.JSONDecodeError, ValueError) as error:
            return SensorReadingModel(
                value=None,
                status_message=f"Resposta inválida: {error}",
                success=False,
            )
        except Exception as error:
            return SensorReadingModel(
                value=None,
                status_message=str(error),
                success=False,
            )

    def _extract_value(self, payload: dict[str, Any]) -> str:
        if isinstance(payload, dict):
            if "value" in payload:
                return str(payload["value"])

            data = payload.get("data")
            if isinstance(data, dict):
                if "value" in data:
                    return str(data["value"])
                if "reading" in data:
                    return str(data["reading"])

            if isinstance(data, list) and data:
                first_item = data[0]
                if isinstance(first_item, dict) and "value" in first_item:
                    return str(first_item["value"])

        raise ValueError("campo de valor não encontrado")
