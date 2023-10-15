#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = "(hbnb)"

    __classes = {
        "BaseModel",
        "User"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id
        """
        args = arg.split()
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in objdict:
                print(objdict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the
        class name and id
        """
        args = arg.split()
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in objdict:
                del objdict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name
        """
        args = arg.split()
        obj_dict = storage.all()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for key, value in obj_dict.items():
                if len(args) == 0 or value.__class__.__name__ == args[0]:
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the
        class name and id by adding or updating attribute
        """
        args = arg.split()
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                tran_type = type(obj.__class__.__dict__[args[2]])
                if tran_type in (str, int, float):
                    obj.__dict__[args[2]] = tran_type(args[3])
                else:
                    obj.__dict__[args[2]] = args[3]
            else:
                obj.__dict__[args[2]] = args[3]
        elif isinstance(argl[2], dict):
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for k, v in args[2].items():
                if k in obj.__class__.__dict__.keys():
                    valtype = type(obj.__class__.__dict__[k])
                    if valtype in (str, int, float):
                        obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v


if __name__ == "__main__":
    HBNBCommand().cmdloop()
