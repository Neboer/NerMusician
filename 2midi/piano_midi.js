var result = []

let body = document.getElementsByTagName("tbody")[0]
for (let tr of body.children) {
    let tds = Array.from(tr.children).map(x => x.textContent)
    if (tds[2].trim().length > 0) {
        result.push({
            midi: Number.parseInt(tds[0]),
            piano_key: Number.parseInt(tds[2]),
            note_name: tds[3],
            frequency: Number.parseFloat(tds[5])
        })
    }
}