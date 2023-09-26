class NutritionTableLoadError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        result = self.message if self.message else "There's some problem with loading file"
        return f"NutritionTableLoadError: {result}"
