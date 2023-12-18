class Item():
  def __init__ (self):
    self.next = None
    self.value = None

class Fila():
  def __init__(self):
    self.first = Item()
    self._tamanho = 0
  def adicionar(self, item):
    p = self.first
    for _ in range(self._tamanho + 1):
      if p.value == None:
        p.value = item
        self._tamanho += 1
      
      elif p.next == None:
        p.next = Item()
        p.next.value = item
        self._tamanho += 1
        
      else:
        p = p.next

  def remover(self, item):
    p = self.first
    for i in range(self._tamanho + 1):
      if p == None:
        raise Exception('Item não encontrado.')
      elif p.value == item:
        e = p
        for _ in range(i, self._tamanho + 1):
          if e.next == None:
            e.value = e.next
          else:
            e.value = e.next.value
            e = e.next
        self._tamanho -= 1
      else:
        p = p.next
  
  def __len__(self):
    return self._tamanho

  def __getitem__(self, index):
    if type(index) != int:
        raise TypeError('Index precisa ser um inteiro.')
    if index >= self._tamanho:
      raise IndexError('Index fora do alcance da fila.')
    while index < 0:
      index = self._tamanho + index
    p = self.first
    for i in range(index + 1):
      if i == index:
        return p.value
      else:
        p = p.next


# Exemplo para testes
fila = Fila()

fila.adicionar(1)
fila.adicionar(2)
fila.adicionar('3')

print(f'item 0: {fila[0]}')
print(f'item 1: {fila[1]}')
print(f'len: {len(fila)}')

fila.remover(2)

print(f'item 0: {fila[0]}')
print(f'item 1: {fila[1]}')
print(f'len: {len(fila)}')