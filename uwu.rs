fn main() {
    use std::io::Write as _;
    let buf = unsafe { std::mem::transmute::<[[u8; 4]; 1024], [u8; 4096]>([*b"uwu\n"; 1024]) };
    let stdout = std::io::stdout();
    let mut stdout = stdout.lock();
    while let Ok(_) = stdout.write_all(&buf) {
        // uwwwuuuuuuuuuu
    }
}