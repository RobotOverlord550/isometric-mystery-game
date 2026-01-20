import json_util


#TODO: Figure out a good consistent json structure to use throughout development to avoid too much refactoring
class TileIndex():
    """Class for loading tile information into memory for reference
    """    
    def __init__(self):
        self.index: dict = {}


    def add_tile_data(self, path):
        """Load tile data (json) into the tile index

        Args:
            path (sys.path or str): path to json to load
        """        
        self.index.update(dict(json_util.get_json_dict(path)))


    def get_index_ref(self) -> dict:
        """get reference to the index stores within the class

        Returns:
            dict: Index as dict
        """        
        return self.index


#TODO: Implement tilemap which can reference a TileIndex and be easily editable as json to avoid me having to make complicated tools
class TileMap():
    pass
        