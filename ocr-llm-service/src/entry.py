from workers import Response, WorkerEntrypoint

class Default(WorkerEntrypoint):

    async def get_llm_response(self, prompt):
        response = await self.env.AI.run('@cf/meta/llama-3.2-3b-instruct', {"prompt": prompt})
        return response.to_py().get("response")

    async def fetch(self, request):
        if "/favicon.ico" in request.url:
            return Response("OK", status=200)
        
        ai_response = await self.get_llm_response("hi")

        return Response(ai_response, status=200)
