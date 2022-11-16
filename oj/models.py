import code
import uuid
from django.db import models
from . import compile

class CompilerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    code = models.TextField()
    #name = models.CharField(max_length=100)
    success = models.CharField(null=True, blank=True, max_length=555)
    fail = models.CharField(null=True, blank=True, max_length=250)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self) -> None:
        with open('form.txt', "w") as c:
                c.write(self.code)
        cj = compile.CompileJava(code=self.code, id=self.id)
        ret = cj.to_file()
        if not ret:
            print("error writing file: ", ret)
        out, err = cj.compile()
        print("Success: ", out)
        print("Error: ", err)

        self.success = out
        self.fail = err
        return super().save()

    def __str__(self) -> str:
        return str(self.code)