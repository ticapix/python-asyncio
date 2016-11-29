in JavaScript

Promise.resolve("Succès").then(function(valeur) {
  console.log(valeur); // "Succès"
}, function(valeur) {
  // n'est pas appelée
});


in Python


async def promise01():
	return "Succès"

async def main():
	try:
		valeur = await promise01()
		print(valeur)
	except Exception as e:
		pass // n'est pas appelée

