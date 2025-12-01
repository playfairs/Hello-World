$message: "Hello, world!";
$color: #4caf50;

.hello {
  color: $color;
  &::before {
    content: $message;
  }
}
