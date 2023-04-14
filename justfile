build:
	docker build -t calendar:latest .

run: build
	docker run \
	  -v /mnt/d/Code/calendar/index.html:/index.html \
	  -v /mnt/d/Code/calendar/count.txt:/count.txt \
	  -v /mnt/d/Code/calendar/template.html:/template.html \
		--rm \
		calendar:latest

test:
	curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

clean:
	docker rm calendar
