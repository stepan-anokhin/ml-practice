class YouTube:
    """Embed YouTube video into the Jupyter Notebook."""

    def __init__(self, code: str, width: int = 560, height: int = 316, title: str = "YouTube video player"):
        self.code = code
        self.width = width
        self.height = height
        self.title = title

    def _repr_html_(self) -> str:
        """Convert to embeddable HTML."""
        return f"""
        <iframe 
            width="{self.width}" 
            height="{self.height}" 
            src="https://www.youtube.com/embed/{self.code}" 
            title="{self.title}" 
            frameborder="0" 
            allow="accelerometer; 
            autoplay; 
            clipboard-write; 
            encrypted-media; 
            gyroscope; 
            picture-in-picture" 
            allowfullscreen>
        </iframe>
        """
