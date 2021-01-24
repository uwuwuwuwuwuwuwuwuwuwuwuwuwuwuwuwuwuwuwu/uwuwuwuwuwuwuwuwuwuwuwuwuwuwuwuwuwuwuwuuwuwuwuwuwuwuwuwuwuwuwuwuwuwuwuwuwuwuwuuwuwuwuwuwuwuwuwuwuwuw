const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut();
    while (true) {
        _ = try stdout.write("uw");
    }
}
