defmodule Looping do
  def infinite do
    IO.write "uwu"
    infinite
  end
end

IO.write "uwu"
Looping.infinite
