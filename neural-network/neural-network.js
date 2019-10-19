let peso = [0, 0, 0];
let sumarization = -1;

const response = (line) => {
    const [primary, seccondary, terciary] = line;
    const vl1 = (primary * peso[0]);
    const vl2 = (seccondary * peso[1]);
    const vl3 = (terciary * peso[2]);
    return (vl1 + vl2 + vl3) > 0 ? 1 : 0;
}

const changepeso = (line, coeficient) => {
    const [primary, seccondary, terciary] = line;
    if (coeficient > 0) {
        peso = [
            (peso[0] + primary),
            (peso[1] + seccondary),
            (peso[2] + terciary)
        ];
    } else {
        peso = [
            (peso[0] - primary),
            (peso[1] - seccondary),
            (peso[2] - terciary)
        ];
    }
}

const process = (train) => {
    for (let index = 0; index < 2; index++) {
        train.forEach((line, i) => {
            const responses = response(line);
            if (responses !== line[3]) {
                if (responses === 0 && line[3] === 1) {
                    changepeso(line, 1);
                }

                if (responses === 1 && line[3] === 0) {
                    changepeso(line, -1);
                }
            }
        });
    }
}

const train = [
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
];
process(train);
console.log('Pesos => ', peso);

const tests = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0]
];

tests.forEach(test => {
    console.log('testes => ', test, response(test) > 0 ? 'P' : 'J')
});
