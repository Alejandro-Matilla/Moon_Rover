
from machine import UART, Pin
from time import ticks_ms, ticks_diff
from config import WIDTH, FOCAL_LENGTH


class Camera:

    def __init__(self, uart_id=0, tx=0, rx=1,
                 baudrate=115200, timeout_ms=500):

        self._uart = UART(
            uart_id,
            baudrate=baudrate,
            tx=Pin(tx),
            rx=Pin(rx),
            timeout=0
        )

        self._buffer = bytearray()
        self._timeout_ms = timeout_ms
        self._last_message = None
        self.focal_length = FOCAL_LENGTH

        self.tag = None

    def update(self):
        """Read available UART bytes without blocking."""

        if self._uart.any():
            data = self._uart.read()

            if data:
                self._buffer.extend(data)

        # Process complete messages
        while b"\n" in self._buffer:

            index = self._buffer.index(10)
            line = bytes(self._buffer[:index])
            del self._buffer[:index + 1]

            self._process(line)

        # Avoid unbounded buffer growth
        if len(self._buffer) > 128:
            self._buffer = bytearray()

        # Invalidate stale detections
        if self._last_message is not None:
            elapsed = ticks_diff(
                ticks_ms(), self._last_message
            )

            if elapsed > self._timeout_ms:
                self.tag = None

    def _process(self, line):
        """Decode an OpenMV message."""

        try:
            message = line.decode().strip()

            if message == "NONE":
                self.tag = None
                self._last_message = ticks_ms()
                return

            parts = message.split(",")

            if len(parts) != 6 or parts[0] != "TAG":
                return

            self.tag = {
                "id": int(parts[1]),
                "x": int(parts[2]),
                "y": int(parts[3]),
                "w": int(parts[4]),
                "h": int(parts[5])
            }

            self._last_message = ticks_ms()

        except (ValueError, UnicodeError):
            pass

    def get_tag(self):
        """Return latest tag data or None."""
        return self.tag

    def tag_detected(self):
        """Return True if a valid tag is visible."""
        return self.tag is not None

    def distance_cm(self):
        distance =  WIDTH * self.focal_length / self.tag["w"]
        return distance
