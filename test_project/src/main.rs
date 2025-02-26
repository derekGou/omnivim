fn main() {
    use rand::Rng;
    use std::io::stdin;
    use std::cmp::Ordering;
    println!("[STARTING...]");
    println!("Guess a number between 1 - 100! ");
    let num: i32 = rand::thread_rng().gen_range(1..=100);

    while true {
        let mut guess = String::new();

        stdin().read_line(&mut guess).expect("[INCORRECT INPUT TYPE]");

        let guess: i32 = strip(guess).parse().expect("[INCORRECT INPUT]");

        println!("You guessed: {}!", guess);

        match guess.cmp(&num) {
            Ordering::Equal => break,
            Ordering::Greater => println!("Your guess was greater then the secret number!"),
            Ordering::Less => println!("Your guess was smaller then the secret number!")
        }
    }
    println!("Your guess was correct! You win!");
}


fn strip(mut string: String) -> String{
    if string.ends_with('\n') {
        string.pop();
    }
    if string.ends_with('\r') {
        string.pop();
    }
    string
}