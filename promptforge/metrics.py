class MetricRegistry:
    """Registry for custom scoring functions."""
    
    def __init__(self):
        self._metrics = {}

    def register(self, name: str, func: callable):
        self._metrics[name] = func

    def get_metric(self, name: str):
        return self._metrics.get(name)

registry = MetricRegistry()
