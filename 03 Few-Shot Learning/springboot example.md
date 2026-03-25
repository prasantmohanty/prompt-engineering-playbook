System:
You are a senior Spring Boot engineer. 
First, think step-by-step in ≤5 concise bullets. 
Then output JSON only with this exact schema:
{
  "steps": string[],                   // 3–5 short bullets
  "files": [                           // code files to create
    {"path": "string", "content": "string"}
  ],
  "next_steps": string[]               // how to run/try
}
Do not include any extra prose outside this JSON.

User:
### Examples (Few-Shot)

Example A — Books API (GET /api/books)
Steps:
1) Define model Book(id,title,author)
2) Service returns a static List<Book>
3) Controller maps GET /api/books -> service.list()
4) Use constructor injection; return JSON list
5) Keep code minimal and self-contained

Output:
{
  "steps": ["model Book","service returns static list","controller GET /api/books","constructor injection","minimal code"],
  "files": [
    {
      "path": "src/main/java/com/example/demo/model/Book.java",
      "content": "package com.example.demo.model;\npublic record Book(String id, String title, String author) {}"
    },
    {
      "path": "src/main/java/com/example/demo/service/BookService.java",
      "content": "package com.example.demo.service;\nimport java.util.List;import com.example.demo.model.Book;import org.springframework.stereotype.Service;\n@Service public class BookService {\n  public List<Book> list(){ return List.of(new Book(\"b-1\",\"Clean Code\",\"Robert Martin\"), new Book(\"b-2\",\"Effective Java\",\"Joshua Bloch\")); }\n}"
    },
    {
      "path": "src/main/java/com/example/demo/web/BookController.java",
      "content": "package com.example.demo.web;\nimport java.util.List;import org.springframework.web.bind.annotation.*;import com.example.demo.model.Book;import com.example.demo.service.BookService;\n@RestController @RequestMapping(\"/api/books\")\npublic class BookController {\n  private final BookService svc; public BookController(BookService svc){ this.svc = svc; }\n  @GetMapping public List<Book> all(){ return svc.list(); }\n}"
    }
  ],
  "next_steps": ["Add Spring Boot starter parent + spring-boot-starter-web in pom.xml","Run the app and GET http://localhost:8080/api/books"]
}

Example B — Users API (GET /api/users)
Steps:
1) Define model User(id,name,email)
2) Service returns a static List<User>
3) Controller exposes GET /api/users
4) Return JSON (no view layer); use constructor injection
5) Keep code concise

Output:
{
  "steps": ["model User","service static list","controller GET /api/users","JSON response","constructor injection"],
  "files": [
    {
      "path": "src/main/java/com/example/demo/model/User.java",
      "content": "package com.example.demo.model;\npublic record User(String id, String name, String email) {}"
    },
    {
      "path": "src/main/java/com/example/demo/service/UserService.java",
      "content": "package com.example.demo.service;\nimport java.util.List;import com.example.demo.model.User;import org.springframework.stereotype.Service;\n@Service public class UserService {\n  public List<User> list(){ return List.of(new User(\"u-1\",\"Asha\",\"asha@example.com\"), new User(\"u-2\",\"Rahul\",\"rahul@example.com\")); }\n}"
    },
    {
      "path": "src/main/java/com/example/demo/web/UserController.java",
      "content": "package com.example.demo.web;\nimport java.util.List;import org.springframework.web.bind.annotation.*;import com.example.demo.model.User;import com.example.demo.service.UserService;\n@RestController @RequestMapping(\"/api/users\")\npublic class UserController {\n  private final UserService svc; public UserController(UserService svc){ this.svc = svc; }\n  @GetMapping public List<User> all(){ return svc.list(); }\n}"
    }
  ],
  "next_steps": ["Ensure spring-boot-starter-web dependency","Run and GET http://localhost:8080/api/users"]
}

### Now solve (Few-Shot + CoT target)

Task:
Create a simple Spring Boot service with one REST endpoint that returns a list of customers.
Each customer has: id, name, email.

Requirements:
- Use Spring Web
- Use a service layer
- Return JSON
- Include a sample controller, service, and model class

Constraints:
- Keep code minimal and production-friendly (constructor injection)
- No extra commentary; JSON output only per schema

Steps:
(Think in ≤5 concise bullets)

Output (JSON only with steps, files, next_steps):