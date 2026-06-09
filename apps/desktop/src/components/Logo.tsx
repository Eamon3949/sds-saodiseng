// 24×24 pixel-art: bald monk with a broom (扫地僧).
// I=ink outline, S=skin, R=robe, G=gold sash, B=broom bristles, H=broom handle

const ROWS = [
  '........................',
  '........................',
  '........................',
  '.......IIIIIIII.........',
  '......ISSSSSSSSI........',
  '.....ISSSSSSSSSI........',
  '.....ISSISSISSSI........',
  '.....ISSSSSSSSSI........',
  '.....ISSSRRRSSSI........',
  '......ISSSSSSI..........',
  '.......IIIIII...........',
  '......IIIRIIII..........',
  '.....IRRRRRRRRII........',
  '....IRRRRGRRRRRI........',
  '....IRRRRGRRRRRI........',
  '....IRRRRRRRRRRIHH......',
  '....IRRRRRRRRRRIHBB.....',
  '....IRRRRRRRRRRIHBBH....',
  '....IRRRRRRRRRRIHHBB....',
  '....IDDDDDDDDDDIIBBBB...',
  '.....IIIIIIIIIIIIHBBB...',
  '..................IHH...',
  '........................',
  '........................',
];

const COLOR: Record<string, string> = {
  I: '#2C1810',   // dark brown ink (matches --ink)
  S: '#F5D5A8',   // warm skin
  R: '#8B6914',   // deep gold robe
  G: '#D4A017',   // bright gold sash
  D: '#5C4830',   // dark hem
  H: '#C08457',   // broom handle (terracotta)
  B: '#E8D9B8',   // broom bristles
  W: '#2C1810',   // eyes (same as ink)
};

export function Logo({ size = 22 }: { size?: number }) {
  const cells: { x: number; y: number; c: string }[] = [];
  for (let y = 0; y < ROWS.length; y++) {
    const row = ROWS[y];
    for (let x = 0; x < row.length; x++) {
      const ch = row[x];
      if (COLOR[ch]) cells.push({ x, y, c: COLOR[ch] });
    }
  }
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" shapeRendering="crispEdges" aria-hidden>
      {cells.map((p, i) => (
        <rect key={i} x={p.x} y={p.y} width={1} height={1} fill={p.c} />
      ))}
    </svg>
  );
}
