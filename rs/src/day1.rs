fn parse_input(input: &str) -> (Vec<usize>, Vec<usize>) {
    let mut left_col: Vec<usize> = Vec::with_capacity(input.len());
    let mut right_col: Vec<usize> = Vec::with_capacity(input.len());
    for line in input.lines() {
        let mut parts = line.split_whitespace();
        let (l, r) = (parts.next().unwrap(), parts.next().unwrap());
        left_col.push(l.parse().unwrap());
        right_col.push(r.parse().unwrap());
    }
    return (left_col, right_col);
}

pub fn part1(input: &str) -> usize {
    let (mut left_col, mut right_col) = parse_input(input);
    left_col.sort();
    right_col.sort();
    left_col
        .iter()
        .zip(right_col.iter())
        .map(|(l, r)| l.abs_diff(*r))
        .sum()
}

pub fn part2(_input: &str) -> usize {
    0
}
