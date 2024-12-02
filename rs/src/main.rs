use reqwest::blocking::Client;
use reqwest::header::{HeaderValue, COOKIE};
use reqwest::Error;
use std::path::Path;
use std::time::Instant;

mod day1;

type PartFn = fn(input: &str) -> usize;

fn run(day: usize, part1_fn: PartFn, part2_fn: PartFn) {
    let input = get_puzzle_input(day).unwrap();

    let start = Instant::now();
    let part1_result = part1_fn(&input);
    let duration_part1 = start.elapsed().as_millis();
    println!("Day {}.1: {} ({} ms)", day, part1_result, duration_part1);

    let start = Instant::now();
    let part2_result = part2_fn(&input);
    let duration_part2 = start.elapsed().as_millis();
    println!("Day {}.2: {} ({} ms)", day, part2_result, duration_part2);
    println!("")
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let days: Vec<usize> = if args.len() > 1 {
        args[1..]
            .iter()
            .filter_map(|d| d.parse::<usize>().ok())
            .collect()
    } else {
        vec![1]
    };

    for day in days {
        match day {
            1 => run(day, day1::part1, day1::part2),
            _ => eprintln!("Invalid day: {}. Skipping...", day),
        }
    }
}

fn get_puzzle_input(day: usize) -> Result<String, Error> {
    dotenv::dotenv().ok();
    // Check if we have the input file alread
    if Path::new(format!("../data/day{}", day).as_str())
        .try_exists()
        .unwrap()
    {
        let data =
            std::fs::read_to_string(format!("../data/day{}", day)).expect("Failed to read file");
        Ok(data)
    } else {
        println!("Fetching input for day {}...", day);
        let session_cookie = std::env::var("SESSION_COOKIE").expect("SESSION_COOKIE not set");

        let url = format!("https://adventofcode.com/2023/day/{}/input", day);
        let client = Client::new();
        let cookie = HeaderValue::from_str(&session_cookie).unwrap();
        let response = client.get(url).header(COOKIE, cookie).send()?.text()?;
        if response.contains("log in") {
            panic!("Invalid session cookie");
        }
        // Store the input for later use
        std::fs::write(format!("../data/day{}", day).as_str(), &response).unwrap();
        Ok(response)
    }
}
