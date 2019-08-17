// Algoritomo para verificar se ouve uma troca de direção
const ccw = (ponto1, ponto2, ponto3) => {
  return (
    (ponto2.x - ponto1.x) *
    (ponto3.y - ponto1.y - (ponto2.y - ponto1.y)) *
    (ponto3.x - ponto1.x) > 0.000001);
}

// adiciona 3 itens a lista e verifica se náo houve curva
// caso houver remove o length - 2 item.
const logica = (listaOrdenada) => {
  const lista = [];
  for (let i = 0; i < listaOrdenada.length; i++) {
    lista.push(listaOrdenada[i]);
    while (lista.length > 2) {
      const [ponto3, ponto2, ponto1] = Object.assign([], lista).reverse();
      if (ccw(ponto1, ponto2, ponto3)) {
        lista.splice((lista.length - 2), 1);
      } else {
        break;
      }
    }
  }
  return lista;
}

// Verifica se a lista é par, sendo par é concavo
const isConcavo = (list) => {
  return list.length & 1 ? 'Convexo' : 'Concavo';
}

// lista com os dados em 2d dos pontos.
let listaOrdenadaGlobal = [
  {
    x: 0,
    y: 0
  },
  {
    x: 0,
    y: 3
  },
  {
    x: 3,
    y: 0
  },
  {
    x: 3,
    y: 3
  }
];

// Obtem a primeira lista de pontos
const listaDePontosSuperiores = logica(listaOrdenadaGlobal);
console.log(listaDePontosSuperiores);

listaOrdenadaGlobal.sort((a, b) => a.y - b.y);

// Obtem a segunda lista de pontos
let listaPontosInferior = logica(listaOrdenadaGlobal);

// Remove os pontos duplicados
listaDePontosSuperiores.forEach(inf01 => {
  listaPontosInferior = listaPontosInferior.filter(inf02 => !(
    inf01.x === inf02.x &&
    inf01.y === inf02.y
  ));
});

console.log(listaPontosInferior);

// Mostra se é concavo ou convexo.
console.log(isConcavo(listaDePontosSuperiores.concat(listaPontosInferior)));