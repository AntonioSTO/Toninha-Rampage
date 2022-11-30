import pygame, csv, os

#######################################################
def img(diretorio):
    return pygame.image.load(diretorio)

def scale(imagem, resolucao):
    return pygame.transform.scale(imagem, resolucao)
#######################################################

#################################################################

i_b1 = scale(img(r'./tileset/bloco1.png'), (32, 32))
i_b3 = scale(img(r'./tileset/bloco3.png'), (32, 32))
i_b14 = scale(img(r'./tileset/bloco14.png'), (32, 32))
i_b28 = scale(img(r'./tileset/bloco28.png'), (32, 32))

#################################################################

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Tilemap:
    def __init__(self, filename, surface):
        self.tile_size = 32
        self.start_x, self.start_y = 0, 0
        self.map_surface = surface
        self.map_surface.set_colorkey((0,0,0))
        self.tiles = self.load_tiles(filename)
        self.load_map()

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '0':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '1':
                    tiles.append(Tile(i_b1, x * self.tile_size, y * self.tile_size))
                elif tile == '3':
                    tiles.append(Tile(i_b3, x * self.tile_size, y * self.tile_size))
                elif tile == '14':
                    tiles.append(Tile(i_b14, x * self.tile_size, y * self.tile_size))
                elif tile == '28':
                    tiles.append(Tile(i_b28, x * self.tile_size, y * self.tile_size))
                x += 1

                    #mover-se à próxima coluna
            y += 1
        
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
    
    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)
    
    def draw_map(self, surface):
        surface.blit(self.map_surface, (0,0))

